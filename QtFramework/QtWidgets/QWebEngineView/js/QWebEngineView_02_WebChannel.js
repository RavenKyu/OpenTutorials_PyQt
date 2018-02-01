new QWebChannel(qt.webChannelTransport, function (channel) {
    handler = channel.objects.handler;
    handler.setText("Hello");  // 연결되자마자 Hello를 쏜다

    // handler 시그널인 getText와 연결
    handler.getText.connect(function(message) {
        console.log("Received message: " + message);
        handler.setText("Succeed")
    });

});