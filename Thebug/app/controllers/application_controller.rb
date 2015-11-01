class ApplicationController < ActionController::API
    $current = "hash";
    #before_filter :authenticate_user_from_token, except: [:token]
    def index
        email = params[:email]
        password = params[:password]
        user = User.find_by(email: email)
        if user && user.password == password
            $current = user.auth_token
            render json: { authenticated: 'True' , token: user.auth_token}
        else
            render json: { authenticated: 'False' }, status: 401
        end
    end
    def show
        puts($current);
    end
end