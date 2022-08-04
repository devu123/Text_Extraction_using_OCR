from appliances.BoschType import get_bosch_model_number
from appliances.ElectroluxType import get_electrolux_model_number
from appliances.FrigidaireType import get_frigidaire_model_number
from appliances.GeType import get_ge_model_number
from appliances.HotpointType import get_hotpoint_model_number
from appliances.KitchenAidType import get_kitchenaid_model_number
from appliances.LgType import get_lg_model_number
from appliances.MaytagType import get_maytag_model_number
from appliances.SamsungType import get_samsung_model_number
from appliances.WhirlpoolType import get_whirlpool_model_number

brands = {"samsung": get_samsung_model_number,
          "ge": get_ge_model_number,
          "lg": get_lg_model_number,
          "bosch": get_bosch_model_number,
          "electrolux": get_electrolux_model_number,
          "frigidaire": get_frigidaire_model_number,
          "hotpoint": get_hotpoint_model_number,
          "kitchenaid": get_kitchenaid_model_number,
          "maytag": get_maytag_model_number,
          "whirlpool": get_whirlpool_model_number}
