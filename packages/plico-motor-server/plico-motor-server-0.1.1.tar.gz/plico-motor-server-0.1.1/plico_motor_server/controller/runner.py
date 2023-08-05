import os
import time
from plico.utils.base_runner import BaseRunner
from plico_motor_server.devices.simulated_motor import \
    SimulatedMotor
from plico_motor_server.devices.picomotor import Picomotor
from plico_motor_server.devices.KURIOSVB1_thorlabs import TunableFilter
from plico_motor_server.devices.FW102B_thorlabs import FilterWheel
from plico_motor_server.devices.PI_motors import PI_E861
from plico.utils.logger import Logger
from plico.utils.control_loop import FaultTolerantControlLoop
from plico.utils.decorator import override
from plico_motor_server.controller.controller import MotorController
from plico.rpc.zmq_ports import ZmqPorts


class Runner(BaseRunner):

    RUNNING_MESSAGE = "Motor controller is running."

    def __init__(self):
        BaseRunner.__init__(self)

    def _createMotorDevice(self):
        motorDeviceSection = self.configuration.getValue(
            self.getConfigurationSection(), 'motor')
        motorModel = self.configuration.deviceModel(motorDeviceSection)
        if motorModel == 'simulatedMotor':
            self._createSimulatedMotor(motorDeviceSection)
        elif motorModel == 'picomotor':
            self._createPicomotor(motorDeviceSection)
        elif motorModel == 'KURIOS-VB1_thorlabs':
            self._createFilterDevice(motorDeviceSection)
        elif motorModel == 'FW102B_thorlabs':
            self._createFilterDevice(motorDeviceSection)
        elif motorModel == 'PI_E861':
            self._createPI_E861(motorDeviceSection)
        else:
            raise KeyError('Unsupported motor model %s' % motorModel)

    def _createSimulatedMotor(self, motorDeviceSection):
        motorName = self.configuration.deviceName(motorDeviceSection)
        self._motor = SimulatedMotor(motorName)

    def _createPicomotor(self, motorDeviceSection):
        name = self.configuration.deviceName(motorDeviceSection)
        ipaddr = self.configuration.getValue(motorDeviceSection, 'ip_address')
        naxis = self.configuration.getValue(
            motorDeviceSection, 'naxis', getint=True)
        timeout = self.configuration.getValue(
            motorDeviceSection, 'comm_timeout', getfloat=True)
        kwargs = {'naxis': naxis, 'timeout': timeout, 'name': name}
        try:
            port = self.configuration.basePort(motorDeviceSection)
            kwargs['port'] = port
        except KeyError:
            pass
        self._motor = Picomotor(ipaddr, **kwargs)
        #     self._motor = Picomotor(ipaddr,
        #                             port=port,
        #                             axis=axis,
        #                             timeout=timeout,
        #                             name=name)
        # else:
        #     self._motor = Picomotor(ipaddr,
        #                             axis=axis,
        #                             timeout=timeout,
        #                             name=name)

    def _createFilterDevice(self, motorDeviceSection):
        name = self.configuration.deviceName(motorDeviceSection)
        usb_port = self.configuration.getValue(
            motorDeviceSection, 'usb_port')
        speed = self.configuration.getValue(
            motorDeviceSection, 'speed', getint=True)
        if name == 'TunableFilter':
            self._motor = TunableFilter(name, usb_port, speed)
        elif name == 'FilterWheel':
            self._motor = FilterWheel(name, usb_port, speed)

    def _createPI_E861(self, motorDeviceSection):
        name = self.configuration.deviceName(motorDeviceSection)
        usb_port = self.configuration.getValue(
            motorDeviceSection, 'usb_port')
        speed = self.configuration.getValue(
            motorDeviceSection, 'speed', getint=True)
        self._motor = PI_E861(name, usb_port, speed)

    def _replyPort(self):
        return self.configuration.replyPort(self.getConfigurationSection())

    def _statusPort(self):
        return self.configuration.statusPort(self.getConfigurationSection())

    def _setUp(self):
        self._logger = Logger.of("Motor Controller runner")

        self._zmqPorts = ZmqPorts.fromConfiguration(
            self.configuration, self.getConfigurationSection())
        self._replySocket = self.rpc().replySocket(
            self._zmqPorts.SERVER_REPLY_PORT)
        self._statusSocket = self.rpc().publisherSocket(
            self._zmqPorts.SERVER_STATUS_PORT, hwm=1)

        self._createMotorDevice()

        self._controller = MotorController(
            self.name,
            self._zmqPorts,
            self._motor,
            self._replySocket,
            self._statusSocket,
            self.rpc())

    def _runLoop(self):
        self._logRunning()

        FaultTolerantControlLoop(
            self._controller,
            Logger.of("Motor Controller control loop"),
            time,
            0.02).start()
        self._logger.notice("Terminated")

    @override
    def run(self):
        self._setUp()
        self._runLoop()
        return os.EX_OK

    @override
    def terminate(self, signal, frame):
        self._controller.terminate()
