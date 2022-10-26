from mss import mss

with mss() as sct:
    sct.shot()


import mss.tools


with mss.mss() as sct:
    # The screen part to capture
    monitor = {"top": 160, "left": 400, "width": 160, "height": 135}
    output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

    # Grab the data
    sct_img = sct.grab(monitor)

    # Save to the picture fil
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
    print(output)