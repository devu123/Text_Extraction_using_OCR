from appliances.classify_device import classify_device
from logger import get_logger

logger = get_logger("classifier")


def main():
    washer_content = "CLOTHES DRYER SAMSUNG ELECTRONICS CO DEL NO. WA44A3205AW/A4 LTD. In Mexico 120/240V~ 60Hz " \
                     "5400W 3WIRE or 4WIRE 09.04.2020"
    drier_content = "CLOTHES DRYER SAMSUNG ELECTRONICS CO DEL NO. DVESSRE100V/A3 LTD. In Mexico 120/240V~ 60Hz " \
                    "5400W 3WIRE or 4WIRE 09.04.2020"
    ref_content = "CLOTHES DRYER SAMSUNG ELECTRONICS CO DEL NO. RF27T5201SR/AA LTD. In Mexico 120/240V~ 60Hz " \
                  "5400W 3WIRE or 4WIRE 09.04.2020"
    dish_content = "CLOTHES DRYER SAMSUNG ELECTRONICS CO DEL NO. DW80R2031US/AA LTD. In Mexico 120/240V~ 60Hz " \
                   "5400W 3WIRE or 4WIRE 09.04.2020"
    error_content = "CLOTHES DRYER SAMSUNG ELECTRONICS CO DEL NO. GF80R2031US/AA LTD. In Mexico 120/240V~ 60Hz " \
                    "5400W 3WIRE or 4WIRE 09.04.2020"

    w = classify_device(washer_content, logger)
    d = classify_device(drier_content, logger)
    r = classify_device(ref_content, logger)
    dw = classify_device(dish_content, logger)
    er = classify_device(error_content, logger)

    print("First item = ", w)
    print("Second item = ", d)
    print("Third item = ", r)
    print("Fourth item = ", dw)
    print("Fifth item = ", er)


if __name__ == '__main__':
    main()
