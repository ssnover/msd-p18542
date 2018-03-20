/*
 * file: buttons.js
 * purpose: Define the callbacks for each button in the web application.
 */

function play_clicked()
{
    // load a route which updates db
    $.post("/set_state", {
        button_clicked: 'play'
    });
}

function pause_clicked()
{
    // load a route which updates db
    $.post("/set_state", {
        button_clicked: 'pause'
    });
}

function stop_clicked()
{
    // load a route which updates db
    $.post("/set_state", {
        button_clicked: 'stop'
    });
}