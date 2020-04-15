function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy';
}

function handleFileSelect(event) {
    event.stopPropagation();
    event.preventDefault();

    var files = evt.dataTransfer.files;
    var file = files[0];
    console.log(file.name);

    var text = "";
    var reader = new FileReader();

    var onload = function (event) {
        text = reader.result;
        parseFile(text);
    };

    reader.onload = onload;
    reader.readAsText(files[0]);

}

function parseFile(text) {
    console.log(text);
}

var dropZone = document.getElementById('drop_zone');
dropZone.addEventListener('dragover', handleDragOver, false);
dropZone.addEventListener('drop', handleFileSelect, false);
