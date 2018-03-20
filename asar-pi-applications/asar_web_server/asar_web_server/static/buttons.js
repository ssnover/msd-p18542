function play_clicked()
{
    // load a route which updates db
    $.post("/set_state", {
        new_state: 'play'
    });
}

function pause_clicked()
{
    // load a route which updates db
    $.post("/set_state", {
        new_state: 'pause'
    });
}

function stop_clicked()
{
    // load a route which updates db
    $.post("/set_state", {
        new_state: 'stop'
    });
}