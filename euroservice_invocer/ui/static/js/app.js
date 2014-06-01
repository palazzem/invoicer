(function(angular) {
    var app = angular.module('invoicer', ['ngRoute', 'ngResource']);

    app.config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'static/views/main.html',
            controller: 'MainController',
            controllerAs: 'main'
        }).otherwise({
            redirectTo: '/'
        });
    }]);
})(angular);
