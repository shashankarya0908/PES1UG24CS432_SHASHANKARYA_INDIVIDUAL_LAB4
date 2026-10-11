from game.game_engine import GameEngine
from game.hit_detection import check_hit
from game.target import Target


def test_hit_detection_inside_circle():
    target = Target(100, 100, radius=25)
    assert check_hit([target], (100, 100)) is target
    assert check_hit([target], (125, 100)) is target
    assert check_hit([target], (100, 125)) is target


def test_hit_detection_outside_circle():
    target = Target(100, 100, radius=25)
    assert check_hit([target], (100, 130)) is None
    assert check_hit([target], (130, 100)) is None
    assert check_hit([target], (100, 65)) is None


def test_combo_and_scoring():
    engine = GameEngine()
    engine.targets = [Target(100, 100, radius=25)]
    engine.handle_click((100, 100))
    assert engine.score == 10
    assert engine.combo == 2

    engine.targets = [Target(100, 100, radius=25)]
    engine.handle_click((100, 100))
    assert engine.score == 30
    assert engine.combo == 3

    engine.handle_click((200, 200))
    assert engine.combo == 1


def test_timer_and_round_reset():
    engine = GameEngine()
    assert engine.round_active is True
    engine.update(dt=31)
    assert engine.time_left == 0.0
    assert engine.round_active is False

    engine.start_new_round()
    assert engine.round_active is True
    assert engine.time_left == 30
    assert engine.score == 0
