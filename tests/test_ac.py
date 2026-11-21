import pytest

import selection_core


@pytest.mark.req("AC-3")
def test_ac3_client_can_change_her_selection(sample_event):
    selection_core.submit_selection(sample_event, "cli_100", ["med_1", "med_2"], ["add_to_album"])
    selection_core.submit_selection(sample_event, "cli_100", ["med_3"], ["add_to_album"])
    assert sample_event["selections"][-1]["media_ids"] == ["med_3"]


@pytest.mark.req("AC-6")
def test_ac6_client_of_another_event_is_rejected(sample_event):
    with pytest.raises(selection_core.SelectionError) as exc:
        selection_core.submit_selection(sample_event, "cli_200", ["med_1"], ["add_to_album"])
    assert exc.value.code == "FORBIDDEN"