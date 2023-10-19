// Constants (used often, don't want to fetch each time)
const baseUrl = window.location.href;
const outputArea = document.getElementById("output-area");

// Remove non-numerical characters from the "latest" inputbox
function cleanLatestValue() {
    latestInput = document.getElementById("latest");
    latest.value = latest.value.replace(/\D/g, "");
}

// Take an input string and an array of string escape pairs, and return an escaped string.
function escapeStringWithPairs(inputString, pairs) {
    var newString = inputString;
    for (const pair of pairs) {
        newString = newString.replaceAll(pair[0], pair[1]);
    }
    return newString;
}

// Update the output area value.
function setDigestUrl() {
    if (document.getElementById("url").value.length > 0) {
        outputArea.value = genDigestUrl()
    } else {
        outputArea.value = ""
    }
    // Keep the output area tall enough to fit its value.
    outputArea.style.height = '';
    outputArea.style.height = (outputArea.scrollHeight + 4) + 'px';
}

// Generate and return the appropriate digest URL.
function genDigestUrl() {

    // Prepare to accept specific input IDs and replacement pairs.
    const inputIds = ["url", "feed-title", "feed-description", "feed-icon", "feed-icon-alt", "item-title", "latest"];
    const replacementPairs = [
        [" ", "%20"],
        ["&", "%26"]
    ]

    // For each non-empty inputbox, tack its (escaped) value onto the forthcoming digest URL.
    var digestUrl = baseUrl;
    for (const inputId of inputIds) {
        value = document.getElementById(inputId).value;
        if (value.length > 0) {
            if (inputId == "url") {
                digestUrl += "?";
            } else {
                digestUrl += "&";
            }
            digestUrl += inputId + "=" + escapeStringWithPairs(value, replacementPairs);
        }
    }
    return digestUrl;

}