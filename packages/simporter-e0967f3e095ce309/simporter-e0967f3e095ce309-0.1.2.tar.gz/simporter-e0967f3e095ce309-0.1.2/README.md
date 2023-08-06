# flask-jwt-auth
Package for an authorization functionality using JWT for Flask framework.

## Settings:

To decode token from another Auth API it's neccessary to set Flask `JWT_SECRET_KEY` env. It also could be required to set `JWT_AUDIENCE` env (default value is `"http://localhost:5000/"`)

## Available functions:
* decode_jwt_token - to get JWT payload
* get_current_user - to get user username or ID (`sub` parameter in JWT)
* jwt_required - decorator to validate JWT token and protect desired endpoints
