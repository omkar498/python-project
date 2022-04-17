from main import *

def test_play_song():
    assert play_song() == 1

def test_reduce_volume():
    assert reduce_volume() == SUCCESS

def test_increase_volume():
    assert increase_volume() == SUCCESS

def test_pause():
    assert pause() == SUCCESS

def test_resume():
    assert resume() == SUCCESS

