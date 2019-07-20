var app = new Vue({
    el: '#app',
    data: {
        console_log: "",
        data_received: {},
        previous_timestamp: 0
    },
    methods: {
        refresh: function ()
        {
            /**
             * Check connection status every second
             */
            let refresh_rate = 0.5;
            let rq = new XMLHttpRequest();
            rq.onreadystatechange = function() {
                if (this.readyState === XMLHttpRequest.DONE) {
                    if (this.status === 200) {
                        const receivedJSON = JSON.parse(this.responseText);
                        if (receivedJSON["0"] !== "__EMPTY") {
                            let current_timestamp = receivedJSON["timestamp"];
                            if (app.previous_timestamp !== current_timestamp) {
                                app.previous_timestamp = current_timestamp;
                                app.data_received = receivedJSON;
                                app.console_log += Object.keys(app.data_received)[0] + ": " +  app.data_received[Object.keys(app.data_received)[0]] + "\n\n";
                            }
                        }
                        else
                            console.log("No runs found.")
                    }
                }
            }.bind(rq, this);
            rq.open("POST", "/refresh", true);
            rq.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
            rq.send();

            setTimeout(this.refresh, refresh_rate*1000);
        },
        reset: function () {
            let rq = new XMLHttpRequest();
            rq.open("GET", "/reset", true);
            rq.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
            rq.send();
            app.console_log = "";
        }
    }
});

app.refresh();