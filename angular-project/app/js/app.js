(function(angular) {
    var app = angular.module('invoicer', ['ngRoute', 'ngResource']);

    app.config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/', {
            templateUrl: 'static/views/main.html'
        }).when('/customers', {
            templateUrl: 'static/views/customers.html',
            controller: 'CustomersController',
            controllerAs: 'customers'
        }).otherwise({
            redirectTo: '/'
        });
    }]);
})(angular);
