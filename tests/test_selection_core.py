"""Example tests (happy path only). They import only selection_core: the lesson 4 test rule."""
import pytest

import selection_core


@pytest.mark.req("REQ-SEL-01")
def test_valid_selection_is_returned(sample_event):
    selection = selection_core.submit_selection(sample_event, "cli_100", ["med_1"], ["add_to_album"])
    assert selection["media_ids"] == ["med_1"]
    assert selection["service_codes"] == ["add_to_album"]


@pytest.mark.req("REQ-SEL-01")
def test_valid_selection_is_recorded_on_the_event(sample_event):
    selection_core.submit_selection(sample_event, "cli_100", ["med_1", "med_2"], ["add_to_album"])
    assert len(sample_event["selections"]) == 1

          
@pytest.mark.req("REQ-SEL-02")     
def test_media_from_another_event_is_rejected(sample_event):     
    with pytest.raises(selection_core.SelectionError) as err:     
        selection_core.submit_selection(     
            sample_event, "cli_100", ["med_9"], ["add_to_album"])     
 
    assert err.value.code == "MEDIA_NOT_IN_EVENT"     


@pytest.mark.req("REQ-SEL-03")
def test_available_services_lists_enabled_services_only(sample_event):
    assert selection_core.available_services(sample_event) == ["add_to_album"]


@pytest.mark.req("REQ-SEL-04")
def test_a_rejected_choice_does_not_change_the_situation(sample_event):
    with pytest.raises(selection_core.SelectionError) as err:
        selection_core.submit_selection(
            sample_event, "cli_100", [], ["add_to_album"])

    assert sample_event["selections"] == []


@pytest.mark.req("REQ-SEL-05")
def test_duplicate_items_are_rejected(sample_event):     
    with pytest.raises(selection_core.SelectionError) as err:     
        selection_core.submit_selection(     
            sample_event, "cli_100", ["med_1", "med_1"], ["add_to_album"])
 
    assert err.value.code == "DUPLICATE_MEDIA"


@pytest.mark.req("REQ-SEL-06")
def test_only_the_client_for_the_event_is_authorized_to_choose(sample_event):
    with pytest.raises(selection_core.SelectionError) as err:     
        selection_core.submit_selection(     
            sample_event, "cli_200", ["med_1"], ["add_to_album"])

    assert err.value.code == "FORBIDDEN"