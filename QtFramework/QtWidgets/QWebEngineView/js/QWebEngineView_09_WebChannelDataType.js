new QWebChannel(qt.webChannelTransport, function (channel) {
    handler = channel.objects.handler;
    handler.webToAppSendData({"data": ["hello", "world", 1, {"A": true, "B": false}]});

    handler.appToWebSendData.connect(function(value) {
        console.log(value);
        handler.webToAppSendData(
            {"data": ["hello", "world", 1, {"A": true, "B": false}]});
        handler.webToAppSendData(
            [1, true, false, {"a": "b"}])
    });

});

