function copyAllVariables() {
    var copyText = document.getElementById("copy-all-target");
    var textarea = document.createElement("textarea");
    textarea.value = copyText.textContent;
    document.body.appendChild(textarea);
    textarea.select();
    textarea.setSelectionRange(0, 99999); 
    document.execCommand("copy");
    document.body.removeChild(textarea);
    alert("Copied to clipboard!");
}
function shareOnWhatsApp() {
    var divContent = document.getElementById("copy-all-target").innerHTML;
    var encodedContent = encodeURIComponent(divContent);
    var whatsappURL = "https://api.whatsapp.com/send?text=" + encodedContent;
    window.open(whatsappURL);
}
function refreshPage() {
    location.reload();
}
