from src.midi_controller import hello_world


def test_instantiation():
    """
    Tests the creation of the flash card.
    """
    hello_world_string = hello_world.run()
    assert isinstance(hello_world_string, str)
