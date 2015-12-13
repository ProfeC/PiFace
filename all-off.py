import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital()

print("\nStopping...")
pfd.output_port.all_off()
