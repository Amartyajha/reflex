from reflex.components.chakra.forms.form import Form
from reflex.event import EventChain
from reflex.vars import BaseVar


def test_render_on_submit():
    """Test that on_submit event chain is rendered as a separate function."""
    submit_it = BaseVar(
        _var_name="submit_it",
        _var_type=EventChain,
    )
    f = Form.create(on_submit=submit_it)
    # type: ignore
    exp_submit_name = f"handleSubmit_{f.handle_submit_unique_name}"
    assert f"onSubmit={{{exp_submit_name}}}" in f.render()["props"]


def test_render_no_on_submit():
    """A form without on_submit should not render a submit handler."""
    f = Form.create()
    for prop in f.render()["props"]:
        assert "onSubmit" not in prop
