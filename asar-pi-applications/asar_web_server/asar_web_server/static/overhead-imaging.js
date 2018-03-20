/*
 * file: overhead-imaging.js
 * purpose: Defines functions for periodically updating the image in the web
 *          web server.
 */

var updating_image = true;

function periodic_call()
{

}


function get_latest_image()
{
    $.ajax (
    {
        type: "GET",
        cache: false,
        url: "/image_stream",
        contentType: "image/jpeg",
        mimeType: "text/plain; charset=x-user-defined",
        success: function(data) {
            //document.getElementById('overhead_view').src = data;
            $("#overhead_view").attr('src', 'data:image/jpeg;base64,' + base64Encode(data));
            //document.getElementById("overhead_view").src = "data:image/jpeg;base64," + base64Encode(data);
        },
        error: function(xhr, error_string, exception) {
            alert("Image Update Failed: " + error_string);
        },
        complete: function() {
            if (updating_image)
            {
                setTimeout(get_latest_image, 500); // Set timer to run function in 500 ms
            }
        },
    });
}

function base64Encode(str)
{
    var CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
    var out = "", i = 0, len = str.length, c1, c2, c3;
    while (i < len)
    {
        c1 = str.charCodeAt(i++) & 0xff;
        if (i == len)
        {
            out += CHARS.charAt(c1 >> 2);
            out += CHARS.charAt((c1 & 0x3) << 4);
            out += "==";
            break;
        }
        c2 = str.charCodeAt(i++);
        if (i == len)
        {
            out += CHARS.charAt(c1 >> 2);
            out += CHARS.charAt(((c1 & 0x3)<< 4) | ((c2 & 0xF0) >> 4));
            out += CHARS.charAt((c2 & 0xF) << 2);
            out += "=";
            break;
        }
        c3 = str.charCodeAt(i++);
        out += CHARS.charAt(c1 >> 2);
        out += CHARS.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
        out += CHARS.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >> 6));
        out += CHARS.charAt(c3 & 0x3F);
    }
    return out;
}