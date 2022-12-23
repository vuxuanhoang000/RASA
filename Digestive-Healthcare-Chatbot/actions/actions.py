from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet
import json

#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
with open("benh-tieu-hoa.json", "r", encoding="utf8") as f:
    benh_db = json.loads(f.read())


def tim_kiem_benh(ten_benh: str):
    ten_benh = ten_benh.lower()
    for benh in benh_db:
        if ten_benh in benh["ten"]:
            return benh
    return None


class ActionAskThongTin(Action):
    def name(self) -> Text:
        return "action_ask_thong_tin"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        ten_benh = tracker.get_slot("benh_tieu_hoa")
        benh = tim_kiem_benh(ten_benh=ten_benh)
        if benh == None:
            dispatcher.utter_message(
                text="Xin lỗi! Có thể bệnh mà bạn nói không nằm trong bộ nhớ của chúng tôi hoặc nó không phải bệnh liên quan đến đường tiêu hóa."
            )
        else:
            dispatcher.utter_message(
                text=f"Tên bệnh: {ten_benh}\n- Khái niệm: {benh['khai_niem']}\n- Nguyên nhân: {benh['nguyen_nhan']}\n- Triệu chứng: {benh['trieu_chung']}\n- Phương pháp điều trị: {benh['phuong_phap_dieu_tri']}"
            )
        return []


class ActionAskKhaiNiem(Action):
    def name(self) -> Text:
        return "action_ask_khai_niem"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        tracker.slots.keys()
        ten_benh = tracker.get_slot("benh_tieu_hoa")
        benh = tim_kiem_benh(ten_benh=ten_benh)
        if benh == None:
            dispatcher.utter_message(
                text="Xin lỗi! Có thể bệnh mà bạn nói không nằm trong bộ nhớ của chúng tôi hoặc nó không phải bệnh liên quan đến đường tiêu hóa."
            )
        else:
            dispatcher.utter_message(
                text=f"Khái niệm bệnh {ten_benh}: {benh['khai_niem']}"
            )
        return []


class ActionAskNguyenNhan(Action):
    def name(self) -> Text:
        return "action_ask_nguyen_nhan"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        ten_benh = tracker.get_slot("benh_tieu_hoa")
        benh = tim_kiem_benh(ten_benh=ten_benh)
        if benh == None:
            dispatcher.utter_message(
                text="Xin lỗi! Có thể bệnh mà bạn nói không nằm trong bộ nhớ của chúng tôi hoặc nó không phải bệnh liên quan đến đường tiêu hóa."
            )
        else:
            dispatcher.utter_message(
                text=f"Nguyên nhân bệnh {ten_benh}: {benh['nguyen_nhan']}"
            )
        return []


class ActionAskTrieuChung(Action):
    def name(self) -> Text:
        return "action_ask_trieu_chung"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        ten_benh = tracker.get_slot("benh_tieu_hoa")
        benh = tim_kiem_benh(ten_benh=ten_benh)
        if benh == None:
            dispatcher.utter_message(
                text="Xin lỗi! Có thể bệnh mà bạn nói không nằm trong bộ nhớ của chúng tôi hoặc nó không phải bệnh liên quan đến đường tiêu hóa."
            )
        else:
            dispatcher.utter_message(
                text=f"Triệu chứng bệnh {ten_benh}: {benh['trieu_chung']}"
            )
        return []


class ActionAskPhuongPhapDieuTri(Action):
    def name(self) -> Text:
        return "action_ask_phuong_phap_dieu_tri"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        ten_benh = tracker.get_slot("benh_tieu_hoa")
        benh = tim_kiem_benh(ten_benh=ten_benh)
        if benh == None:
            dispatcher.utter_message(
                text="Xin lỗi! Có thể bệnh mà bạn nói không nằm trong bộ nhớ của chúng tôi hoặc nó không phải bệnh liên quan đến đường tiêu hóa."
            )
        else:
            dispatcher.utter_message(
                text=f"Phương pháp điều trị bệnh {ten_benh}: {benh['phuong_phap_dieu_tri']}"
            )
        return []


class ActionAskSlotsValues(Action):
    def name(self) -> Text:
        return "action_ask_slots_values"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        trieu_chung = {k: 1 if v else 0 for k, v in tracker.slots.items()}
        if trieu_chung["xuat_huyet_da_day"] == 1:
            s = self.tinh_s(
                trieu_chung=[
                    trieu_chung["xuat_huyet_da_day"],
                    trieu_chung["roi_loan_tieu_hoa"],
                    trieu_chung["dau_vung_thuong_vi"],
                    trieu_chung["an_uong_kem"],
                    trieu_chung["dau_dau"],
                    trieu_chung["non_ra_mau"],
                    trieu_chung["buon_non"],
                ],
                he_so=[7, 3, 7, 1, 3, 3, 3],
            )
            dispatcher.utter_message(
                response="utter_slots_values", benh="sa dạ dày", s=s
            )
        elif trieu_chung["nong_rat_da_day"] == 1:
            if trieu_chung["dau_nhoi_xuong_suon"] == 1:
                s = self.tinh_s(
                    trieu_chung=[
                        trieu_chung["nong_rat_da_day"],
                        trieu_chung["dau_nhoi_xuong_suon"],
                        trieu_chung["dau_quanh_ron"],
                        trieu_chung["mot_ran"],
                        trieu_chung["tieu_chay"],
                        trieu_chung["phan_dinh_mau"],
                    ],
                    he_so=[7, 7, 7, 3, 5, 5],
                )
                dispatcher.utter_message(
                    response="utter_slots_values", benh="rối loạn dạ dày", s=s
                )
            elif trieu_chung["dau_tuc_nguc"] == 1:
                s = self.tinh_s(
                    trieu_chung=[
                        trieu_chung["nong_rat_da_day"],
                        trieu_chung["dau_tuc_nguc"],
                        trieu_chung["viem_hong"],
                        trieu_chung["buon_non"],
                        trieu_chung["an_uong_kem"],
                        trieu_chung["o_hoi_o_chua"],
                        trieu_chung["mieng_tiet_nhieu_nuoc_bot"],
                    ],
                    he_so=[7, 7, 3, 3, 1, 3, 3],
                )
                dispatcher.utter_message(
                    response="utter_slots_values", benh="trào ngược dạ dày", s=s
                )
            else:
                dispatcher.utter_message(text="Không thể chẩn đoán được bệnh :(")
        else:
            if trieu_chung["sa_bui_tri"] == 1:
                s = self.tinh_s(
                    trieu_chung=[
                        trieu_chung["sa_bui_tri"],
                        trieu_chung["phan_dinh_mau"],
                        trieu_chung["dau_vung_hau_mon"],
                        trieu_chung["mot_ran"],
                    ],
                    he_so=[7, 5, 7, 3],
                )
                dispatcher.utter_message(response="utter_slots_values", benh="trĩ", s=s)
            elif trieu_chung["xung_quanh_hau_mon"] == 1:
                s = self.tinh_s(
                    trieu_chung=[
                        trieu_chung["xung_quanh_hau_mon"],
                        trieu_chung["dau_vung_hau_mon"],
                        trieu_chung["met_moi_suy_nhuoc"],
                        trieu_chung["phan_dinh_mau"],
                    ],
                    he_so=[5, 7, 1, 5],
                )
                dispatcher.utter_message(
                    response="utter_slots_values", benh="nứt kẽ hậu môn", s=s
                )
            else:
                if trieu_chung["chan_tay_lanh_da_kho_mat_trung"] == 1:
                    s = self.tinh_s(
                        trieu_chung=[
                            trieu_chung["chan_tay_lanh_da_kho_mat_trung"],
                            trieu_chung["tieu_chay"],
                            trieu_chung["met_moi_suy_nhuoc"],
                        ],
                        he_so=[3, 5, 1],
                    )
                    dispatcher.utter_message(
                        response="utter_slots_values", benh="tiêu chảy", s=s
                    )
                elif trieu_chung["da_san_sui_tho_rap"] == 1:
                    s = self.tinh_s(
                        trieu_chung=[
                            trieu_chung["da_san_sui_tho_rap"],
                            trieu_chung["dai_tien_it"],
                            trieu_chung["phan_cung"],
                            trieu_chung["dau_khi_di_dai_tien"],
                        ],
                        he_so=[3, 3, 3, 7],
                    )
                    dispatcher.utter_message(
                        response="utter_slots_values", benh="táo bón", s=s
                    )
                else:
                    if trieu_chung["sot"] == 1:
                        s = self.tinh_s(
                            trieu_chung=[
                                trieu_chung["sot"],
                                trieu_chung["dau_ben_trai_bung_duoi"],
                                trieu_chung["tieu_chay_dai_tien_it_phan_cung"],
                                trieu_chung["an_uong_kem"],
                                trieu_chung["buon_non"],
                                trieu_chung["phan_dinh_mau"],
                            ],
                            he_so=[3, 7, 5, 1, 3, 5],
                        )
                        dispatcher.utter_message(
                            response="utter_slots_values", benh="viêm túi thừa", s=s
                        )
                    else:
                        s = self.tinh_s(
                            trieu_chung=[
                                trieu_chung["dau_vung_thuong_vi"],
                                trieu_chung["tieu_chay_dai_tien_it_phan_cung"],
                                trieu_chung["mat_ngu"],
                                trieu_chung["buon_non"],
                                trieu_chung["o_hoi_o_chua"],
                            ],
                            he_so=[7, 5, 1, 3, 3],
                        )
                        dispatcher.utter_message(
                            response="utter_slots_values",
                            benh="viêm loét dạ dày tá tràng",
                            s=s,
                        )
        return [SlotSet(k, None) for k in trieu_chung.keys()]

    @staticmethod
    def tinh_s(trieu_chung: List, he_so: List) -> str:
        tmp = [trieu_chung[i] * he_so[i] for i in range(len(he_so))]
        s = (sum(tmp) * 100) / sum(he_so)
        return f"{s:.2f}"


class ValidateChanDoanBenhForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_chan_doan_benh_form"

    def validate_xuat_huyet_da_day(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"xuat_huyet_da_day": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "roi_loan_tieu_hoa",
                "dau_vung_thuong_vi",
                "an_uong_kem",
                "dau_dau",
                "non_ra_mau",
                "buon_non",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["xuat_huyet_da_day"] = True
        else:
            result["xuat_huyet_da_day"] = False
            ignored_slots = ["roi_loan_tieu_hoa", "dau_dau", "non_ra_mau"]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_roi_loan_tieu_hoa(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"roi_loan_tieu_hoa": True}
        else:
            return {"roi_loan_tieu_hoa": False}

    def validate_dau_dau(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dau_dau": True}
        else:
            return {"dau_dau": False}

    def validate_non_ra_mau(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"non_ra_mau": True}
        else:
            return {"non_ra_mau": False}

    def validate_nong_rat_da_day(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"nong_rat_da_day": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "dau_nhoi_xuong_suon",
                "dau_quanh_ron",
                "mot_ran",
                "tieu_chay",
                "phan_dinh_mau",
                "dau_tuc_nguc",
                "viem_hong",
                "buon_non",
                "an_uong_kem",
                "o_hoi_o_chua",
                "mieng_tiet_nhieu_nuoc_bot",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["nong_rat_da_day"] = True
        else:
            result["nong_rat_da_day"] = False
            ignored_slots = [
                "dau_nhoi_xuong_suon",
                "dau_quanh_ron",
                "dau_tuc_nguc",
                "viem_hong",
                "mieng_tiet_nhieu_nuoc_bot",
            ]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_dau_nhoi_xuong_suon(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"dau_nhoi_xuong_suon": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "nong_rat_da_day",
                "dau_nhoi_xuong_suon",
                "dau_quanh_ron",
                "mot_ran",
                "tieu_chay",
                "phan_dinh_mau",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["dau_nhoi_xuong_suon"] = True
        else:
            result["dau_nhoi_xuong_suon"] = False
            ignored_slots = [
                "dau_quanh_ron",
            ]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_dau_quanh_ron(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dau_quanh_ron": True}
        else:
            return {"dau_quanh_ron": False}

    def validate_dau_tuc_nguc(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"dau_tuc_nguc": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "nong_rat_da_day",
                "dau_tuc_nguc",
                "viem_hong",
                "buon_non",
                "an_uong_kem",
                "o_hoi_o_chua",
                "mieng_tiet_nhieu_nuoc_bot",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["dau_tuc_nguc"] = True
        else:
            result["dau_tuc_nguc"] = False
            ignored_slots = [
                "mot_ran",
                "tieu_chay",
                "phan_dinh_mau",
                "viem_hong",
                "buon_non",
                "an_uong_kem",
                "o_hoi_o_chua",
                "mieng_tiet_nhieu_nuoc_bot",
            ]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_viem_hong(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"viem_hong": True}
        else:
            return {"viem_hong": False}

    def validate_mieng_tiet_nhieu_nuoc_bot(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"mieng_tiet_nhieu_nuoc_bot": True}
        else:
            return {"mieng_tiet_nhieu_nuoc_bot": False}

    def validate_sa_bui_tri(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"sa_bui_tri": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "phan_dinh_mau",
                "dau_vung_hau_mon",
                "mot_ran",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["sa_bui_tri"] = True
        else:
            ignored_slots = [
                "mot_ran",
            ]
            for slot in ignored_slots:
                result[slot] = False
            result["sa_bui_tri"] = False
        return result

    def validate_mot_ran(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"mot_ran": True}
        else:
            return {"mot_ran": False}

    def validate_xung_quanh_hau_mon(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"xung_quanh_hau_mon": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "dau_vung_hau_mon",
                "buon_non",
                "an_uong_kem",
                "o_hoi_o_chua",
                "mieng_tiet_nhieu_nuoc_bot",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["xung_quanh_hau_mon"] = True
        else:
            result["xung_quanh_hau_mon"] = False
            ignored_slots = [
                "dau_vung_hau_mon",
            ]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_dau_vung_hau_mon(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dau_vung_hau_mon": True}
        else:
            return {"dau_vung_hau_mon": False}

    def validate_chan_tay_lanh_da_kho_mat_trung(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"chan_tay_lanh_da_kho_mat_trung": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = ["tieu_chay", "met_moi_suy_nhuoc"]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["chan_tay_lanh_da_kho_mat_trung"] = True
        else:
            result["chan_tay_lanh_da_kho_mat_trung"] = False
            ignored_slots = ["tieu_chay"]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_tieu_chay(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"tieu_chay": True}
        else:
            return {"tieu_chay": False}

    def validate_da_san_sui_tho_rap(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"da_san_sui_tho_rap": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = ["dai_tien_it", "phan_cung", "dau_khi_di_dai_tien"]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["da_san_sui_tho_rap"] = True
        else:
            result["da_san_sui_tho_rap"] = False
            ignored_slots = ["dai_tien_it", "phan_cung", "dau_khi_di_dai_tien"]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_dai_tien_it(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dai_tien_it": True}
        else:
            return {"dai_tien_it": False}

    def validate_phan_cung(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"phan_cung": True}
        else:
            return {"phan_cung": False}

    def validate_dau_khi_di_dai_tien(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dau_khi_di_dai_tien": True}
        else:
            return {"dau_khi_di_dai_tien": False}

    def validate_sot(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        result = {"sot": None}
        value = str(slot_value).lower()
        if value == "có":
            required_slots = [
                "sot",
                "dau_ben_trai_bung_duoi",
                "tieu_chay_dai_tien_it_phan_cung",
                "an_uong_kem",
                "buon_non",
                "phan_dinh_mau",
            ]
            for slot in tracker.slots.keys():
                if slot not in required_slots:
                    result[slot] = False
            result["sot"] = True
        else:
            result["sot"] = False
            ignored_slots = ["dau_ben_trai_bung_duoi", "an_uong_kem"]
            for slot in ignored_slots:
                result[slot] = False
        return result

    def validate_dau_ben_trai_bung_duoi(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dau_ben_trai_bung_duoi": True}
        else:
            return {"dau_ben_trai_bung_duoi": False}

    def validate_an_uong_kem(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"an_uong_kem": True}
        else:
            return {"an_uong_kem": False}

    def validate_phan_dinh_mau(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"phan_dinh_mau": True}
        else:
            return {"phan_dinh_mau": False}

    def validate_dau_vung_thuong_vi(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"dau_vung_thuong_vi": True}
        else:
            return {"dau_vung_thuong_vi": False}

    def validate_tieu_chay_dai_tien_it_phan_cung(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"tieu_chay_dai_tien_it_phan_cung": True}
        else:
            return {"tieu_chay_dai_tien_it_phan_cung": False}

    def validate_mat_ngu(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"mat_ngu": True}
        else:
            return {"mat_ngu": False}

    def validate_buon_non(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"buon_non": True}
        else:
            return {"buon_non": False}

    def validate_met_moi_suy_nhuoc(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"met_moi_suy_nhuoc": True}
        else:
            return {"met_moi_suy_nhuoc": False}

    def validate_o_hoi_o_chua(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        value = str(slot_value).lower()
        if value == "có":
            return {"o_hoi_o_chua": True}
        else:
            return {"o_hoi_o_chua": False}
