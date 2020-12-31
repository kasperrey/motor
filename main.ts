input.onButtonPressed(Button.A, function () {
    radio.sendValue("name", 1)
})
input.onGesture(Gesture.TiltRight, function () {
    radio.sendValue("name", 5)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendValue("name", 3)
})
input.onButtonPressed(Button.B, function () {
    radio.sendValue("name", 2)
})
radio.onReceivedValue(function (name, value) {
    if (value == 1) {
        powerfunctions.setSpeed(PowerFunctionsMotor.Red1, 1)
    }
    if (value == 2) {
        powerfunctions.setSpeed(PowerFunctionsMotor.Red1, 2)
    }
    if (value == 3) {
        powerfunctions.setSpeed(PowerFunctionsMotor.Red1, 3)
    }
    if (value == 4) {
        powerfunctions.setMotorDirection(PowerFunctionsMotor.Red1, PowerFunctionsDirection.Left)
    }
    if (value == 5) {
        powerfunctions.setMotorDirection(PowerFunctionsMotor.Red1, PowerFunctionsDirection.Right)
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    radio.sendValue("name", 4)
})
powerfunctions.connectIrLed(AnalogPin.P0)
