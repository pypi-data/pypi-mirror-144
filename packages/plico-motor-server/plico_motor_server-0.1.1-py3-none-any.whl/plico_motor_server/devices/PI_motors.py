'''
Authors
  - A. Puglisi: written in 2022
'''
import abc
import time

from plico.utils.logger import Logger
from plico.utils.decorator import override
from plico_motor_server.devices.abstract_motor import AbstractMotor
from plico_motor.types.motor_status import MotorStatus


class GCSException(Exception):
    pass

def _reconnect(f):
    '''
    Make sure that the function is executed
    after connecting to the motor, and trigger
    a reconnect in the next command if any error occurs.

    Any communication problem will raise a FilterWheelException
    '''
    def func(self, *args, **kwargs):
        try:
            if not self.gcs:
                self.connect()
            return f(self, *args, **kwargs)
        except OSError:
            self.disconnect()
            raise GCSException('Error communicating with PI controller. Will retry...')
        except GCSException:
            raise

    return func

 
class PIGCS_Motor(AbstractMotor):
    '''
    Motor using the PI GCS communication protocol with a serial or USB connection.
    Makes use of the pipython module: https://github.com/PI-PhysikInstrumente/PIPython
    pipython is imported lazily and does not need to be installed until
    an instance of this class is initialized.
    '''

    def __init__(self, name, port, speed):
        from pipython import GCSDevice # Not used here, but let's fail now instead of later
        self._name = name
        self.port = port
        self.speed = speed
        self.naxis = 1
        self.gcs = None
        self.use_servo = False
        self.referenced = [False] * self.naxis
        self.home_timeout = 10  # seconds
        self.steps_to_PIsteps = 1  # In case we want to use smaller steps than PI ones
        self._logger = Logger.of('GCS')
        self._last_commanded_position = [0] * self.naxis

    def connect(self):
        if self.gcs is None:
            from pipython import GCSDevice
            self._logger.notice('Connecting to GCS device at %s' % self.port)
            self.gcs = GCSDevice()
            self.gcs.ConnectRS232(self.port, self.speed)
        else:
            print ("Already connected")
        refdict = self.gcs.qFRF()
        for n in range(self.naxis):
            self.referenced[n] = refdict['%d' % (n+1,)]

    def disconnect(self):
        if self.gcs is not None:
            self.gcs.close()
            self.gcs = None

    @override
    def naxes(self):
        return self.naxis

    @override
    def name(self):
        return self._name

    @override
    def home(self, axis):
        self.referenced[axis-1] = False
        self.gcs.FRF(axis)
        now = time.time()
        while True:
            if time.time() - now > self.home_timeout:
                raise GCSException('Timeout waiting for homing movement')
            time.sleep(0.1)
            if self.gcs.qFRF(axis)[axis]:
                break
        if self.use_servo:
            self.gcs.SVO(axis, 1)
        self.referenced[axis-1] = True

    @_reconnect
    @override
    def position(self, axis):
        posdict = self.gcs.qPOS(axis)
        return round(posdict[axis] / self.steps_to_PIsteps)

    @override
    def move_to(self, axis, position_in_steps):
        self.gcs.MOV(axis, position_in_steps * self.steps_to_PIsteps)

    @override
    def stop(self, axis):
        raise GCSException('Stop command is not supported')

    @override
    def deinitialize(self, axis):
        raise GCSException('Deinitialize command is not supported')

    @abc.abstractmethod
    def steps_per_SI_unit(self, axis):
        '''Derived class must reimplement this method'''
        pass

    @override
    def was_homed(self, axis):
        return self.referenced[axis-1]

    @override
    def type(self, axis):
        return MotorStatus.TYPE_LINEAR

    @override
    def is_moving(self, axis):
        movingdict = self.gcs.IsMoving(axis)
        return movingdict[axis]

    @override
    def last_commanded_position(self, axis):
        return self._last_commanded_position[axis - 1]


class PI_E861(PIGCS_Motor):
    '''
    Specialization of PIGCS_Motor for the PI E-861 controller.
    This class sets the "use_servo" flag to True in order
    to enable the servo loop after initialization.
    '''
    def __init__(self, name, port, speed):
        super().__init__(name, port, speed)
        self.use_servo = True
        self.steps_to_PIsteps = 1e-6  # PI E-861 uses mm as its unit

    def steps_per_SI_unit(self, axis):
        return 1e9

