class UserSerializer < ActiveModel::Serializer
  attributes :id, :email, :created_at , :password , :auth_token , :username#TODO remove password when launched
    has_many :projects
    has_many :issues
end
