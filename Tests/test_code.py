import builtins
import math
import re

import barbie_adventure as ba


def mock_inputs(monkeypatch, inputs):
    """
    Replace input() so each call returns the next value from inputs.
    """
    it = iter(str(i) for i in inputs)

    def fake_input(prompt=""):
        return next(it)

    monkeypatch.setattr(builtins, "input", fake_input)


def test_beach_adventure(monkeypatch, capsys):
    # INPUTS
    mock_inputs(monkeypatch, [
        4,      # Number of people
        30.00,  # Beach chairs
        10.00,  # Sunscreen
        5.00,   # Ice cream
        15.00   # Beach toys
    ])

    # RUN
    total, discounted, per_person, people = ba.beach_day_challenge()
    output = capsys.readouterr().out

    # RETURNS
    assert people == 4
    assert math.isclose(total, 60.00, abs_tol=0.01)
    assert math.isclose(discounted, 53.50, abs_tol=0.01)
    assert math.isclose(per_person, 13.38, abs_tol=0.01)

    # OUTPUT TEXT
    assert "Total cost before discounts: $60.00" in output
    assert "Total cost after discounts: $53.50" in output
    assert "Each person's share: $13.38" in output


def test_escape_plan(monkeypatch, capsys):
    # INPUTS
    mock_inputs(monkeypatch, [
        100, 50,   # Route 1
        120, 70,   # Route 2
        140, 60    # Route 3
    ])

    # RUN
    t1, t2, t3, fastest, saved = ba.escape_plan_challenge()
    output = capsys.readouterr().out

    # RETURNS
    assert math.isclose(t1, 2.00, abs_tol=0.01)
    assert math.isclose(t2, 1.71, abs_tol=0.01)
    assert math.isclose(t3, 2.33, abs_tol=0.01)
    assert math.isclose(fastest, 1.71, abs_tol=0.01)
    assert math.isclose(saved, 0.62, abs_tol=0.01)

    # OUTPUT TEXT
    assert "Time required for Route 1: 2.00 hours" in output
    assert "Time required for Route 2: 1.71 hours" in output
    assert "Time required for Route 3: 2.33 hours" in output
    assert "The fastest route takes 1.71 hours." in output
    assert "Time saved by choosing the fastest route: 0.62 hours" in output


def test_societal_reformation(monkeypatch, capsys):
    # INPUTS
    mock_inputs(monkeypatch, [
        20,  # Total proposed changes
        13   # Successful changes
    ])

    # RUN
    percent, needed, remaining = ba.society_reformation_challenge()
    output = capsys.readouterr().out

    # RETURNS
    assert math.isclose(percent, 65.00, abs_tol=0.01)
    assert needed == 2
    assert remaining == 7

    # OUTPUT TEXT
    assert "Percentage of successful changes: 65.00%" in output
    assert "Number of additional changes needed to achieve a 75% success rate: 2" in output
    assert "Remaining changes to be implemented: 7" in output
