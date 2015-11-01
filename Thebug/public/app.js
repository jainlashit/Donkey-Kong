var routerApp = angular.module('routerApp', ['ui.router','ngCookies']);

routerApp.config(function($stateProvider, $urlRouterProvider) {
    
    $urlRouterProvider.otherwise('/home');
    $stateProvider
        .state("#",{
            url: '/home',
            templateUrl : 'home.html',
            controller : 'homeCtrl'
        })

        .state("users",{
            url: '/users',
            templateUrl : 'user.html',
            controller : 'userCtrl'
        })
    
        .state("logout",{
            url: '/home',
            templateUrl : 'home.html',
            controller : 'homeCtrl'
        })

        .state("login",{
            url: '/login',
            templateUrl : 'login.html',
            controller : 'loginCtrl'
        })

        .state("signup",{
            url: '/signup',
            templateUrl : 'signup.html',
            controller :'signupCtrl'
        })

        .state("home", {
            url: '/home',
            templateUrl: 'home.html',
            controller :  'homeCtrl'
        })
        
        .state("project", {
            url: '/project',
            templateUrl:'project.html',
            controller : 'projectCtrl'
        })

        .state("create_project", {
            url: '/create',
            templateUrl:'create.html',
            controller : 'createCtrl'
        })

        .state("issue" , {
            url: '/issue',
            templateUrl:'issue.html',
            controller : 'issueCtrl'
        })

        .state("notifications",{
            url: '/notifications',
            templateUrl:'notifications.html',
            controller : 'notificationCtrl'
        })
    
        .state("create_issue", {
            url: '/createissue',
            templateUrl:'createissue.html',
            controller : 'createissueCtrl'
        });

        
});