from random import randint
from time import sleep
import pifacedigitalio

DELAY = 0.25  # seconds
pfd = pifacedigitalio.PiFaceDigital()
listener = pifacedigitalio.InputEventListener(chip=pfd)

def toggle_led(event):
	event.chip.leds[event.pin_num].toggle()
	print(event)
	
def stop(event):
	print(event)
	raise SystemExit

try:

	listener.register(0, pifacedigitalio.IODIR_FALLING_EDGE, toggle_led)
	listener.register(1, pifacedigitalio.IODIR_FALLING_EDGE, toggle_led)
	listener.register(3, pifacedigitalio.IODIR_FALLING_EDGE, stop)
	listener.activate()

	if __name__ == "__main__":
		# Turn all the lights on
		# pfd.output_port.all_on()

		# Randomly toggle the lights on and off
		while True:
			r = randint(2,7)
			print(r)

			pfd.leds[r].toggle()
			sleep(DELAY)

			# pfd.leds[6].toggle()
			# sleep(DELAY)

			# pfd.leds[5].toggle()
			# sleep(DELAY)

			# pfd.leds[4].toggle()
			# sleep(DELAY)

			# pfd.leds[3].toggle()
			# sleep(DELAY)

except KeyboardInterrupt:
	# exits when you press CTRL+C
	print("\nStopping...")
	pfd.output_port.all_off()

finally:
	pifacedigitalio.core.deinit()
	listener.deactivate()
