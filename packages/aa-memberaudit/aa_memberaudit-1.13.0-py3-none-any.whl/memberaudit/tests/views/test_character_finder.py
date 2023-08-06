from django.test import RequestFactory, TestCase
from django.urls import reverse
from eveuniverse.models import EveSolarSystem

from app_utils.testing import create_user_from_evecharacter

from ...models import CharacterLocation, Location
from ...views.character_finder import character_finder, character_finder_data
from ..testdata.load_entities import load_entities
from ..testdata.load_eveuniverse import load_eveuniverse
from ..testdata.load_locations import load_locations
from ..utils import (
    add_auth_character_to_user,
    add_memberaudit_character_to_user,
    json_response_to_python_2,
)

MODULE_PATH = "memberaudit.views.character_finder"


class TestCharacterFinderViews(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.factory = RequestFactory()
        load_eveuniverse()
        load_entities()
        load_locations()
        cls.user, _ = create_user_from_evecharacter(
            1001,
            permissions=[
                "memberaudit.basic_access",
                "memberaudit.finder_access",
                "memberaudit.view_same_corporation",
            ],
        )

    def test_can_open_character_finder_view(self):
        # given
        request = self.factory.get(reverse("memberaudit:character_finder"))
        request.user = self.user
        # when
        response = character_finder(request)
        # then
        self.assertEqual(response.status_code, 200)

    def test_character_finder_data(self):
        # given
        character_1001 = add_memberaudit_character_to_user(self.user, 1001)
        jita = EveSolarSystem.objects.get(name="Jita")
        jita_44 = Location.objects.get(id=60003760)
        CharacterLocation.objects.create(
            character=character_1001, eve_solar_system=jita, location=jita_44
        )
        add_memberaudit_character_to_user(self.user, 1002)
        add_auth_character_to_user(self.user, 1003)
        request = self.factory.get(reverse("memberaudit:character_finder_data"))
        request.user = self.user
        # when
        response = character_finder_data(request)
        # then
        self.assertEqual(response.status_code, 200)
        data = json_response_to_python_2(response)
        self.assertSetEqual({x["character_id"] for x in data}, {1001, 1002, 1003})
        first = data[0]
        self.assertSetEqual(
            set(first.keys()),
            {
                "character_id",
                "character",
                "character_organization",
                "main_character",
                "main_organization",
                "state_name",
                "actions",
                "alliance_name",
                "corporation_name",
                "main_alliance_name",
                "main_corporation_name",
                "main_str",
                "unregistered_str",
            },
        )
