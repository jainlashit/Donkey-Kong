class User < ActiveRecord::Base
    before_create -> { self.auth_token = SecureRandom.hex }
    has_many :projects
	has_many :issues
end
