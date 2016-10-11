var app = angular.module('myApp',[]);
app.controller('myController', function($http, $scope){
    var myCtrl = this;
    $scope.me = 'Amit';
    myCtlr.t = ''
    myCtrl.try1 = function(){
        myCtrl.t = ' Amit';
    };
});