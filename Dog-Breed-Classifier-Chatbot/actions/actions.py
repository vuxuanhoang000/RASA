from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pandas as pd

from testing import predict_breed

inf_of_dog_breeds_df = pd.read_csv("information-of-dog-breeds.csv")


def get_dog_random(removed=None, quantity=1):
    if removed == None:
        return inf_of_dog_breeds_df.sample(n=quantity)
    else:
        new_df = inf_of_dog_breeds_df.loc[inf_of_dog_breeds_df["dog_breed"] != removed]
        return new_df.sample(n=quantity)


def get_quick_reply(removed=None):
    dogs_inf = get_dog_random(removed=removed, quantity=3)
    q1 = {
        "content_type": "text",
        "title": "Chó " + dogs_inf["dog_breed"].values[0],
        "image_url": dogs_inf["image"].values[0],
        "payload": "Thông tin về giống chó " + dogs_inf["dog_breed"].values[0],
    }
    q2 = {
        "content_type": "text",
        "title": "Chó " + dogs_inf["dog_breed"].values[1],
        "image_url": dogs_inf["image"].values[1],
        "payload": "Thông tin về giống chó " + dogs_inf["dog_breed"].values[1],
    }
    q3 = {
        "content_type": "text",
        "title": "Chó " + dogs_inf["dog_breed"].values[2],
        "image_url": dogs_inf["image"].values[2],
        "payload": "Thông tin về giống chó " + dogs_inf["dog_breed"].values[2],
    }
    message = {
        # "text": "Xem thêm thông tin về các giống chó khác",
        "quick_replies": [q1, q2, q3],
    }
    return message


class ActionInfoDogBreeds(Action):
    def name(self) -> Text:
        return "action_info_dog_breeds"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        if tracker.latest_message["text"].startswith("http"):
            image_url = tracker.latest_message["text"]
            dispatcher.utter_message(text=f"Đây là chó {predict_breed(image_url)}")
        else:
            dog_breed_name = tracker.latest_message["entities"][0]["value"]
            dog_breed_inf = inf_of_dog_breeds_df.loc[
                inf_of_dog_breeds_df["dog_breed"] == dog_breed_name
            ]
            dispatcher.utter_message(
                text=dog_breed_inf["description"].values[0],
                image=dog_breed_inf["image"].values[0],
            )
            dispatcher.utter_message(
                json_message=get_quick_reply(
                    removed=dog_breed_inf["dog_breed"].values[0]
                )
            )
        return []


class ActionRandom(Action):
    def name(self) -> Text:
        return "action_random"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:

        dog_inf = get_dog_random()
        dispatcher.utter_message(
            text=dog_inf["description"].values[0], image=dog_inf["image"].values[0]
        )
        dispatcher.utter_message(
            json_message=get_quick_reply(removed=dog_inf["dog_breed"].values[0])
        )
        return []
