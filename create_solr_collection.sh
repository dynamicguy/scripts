#!/usr/bin/env sh

curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/branches
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/cats
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/cities
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/companies
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/configs
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/countries
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/locations
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/manufacturers
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/regions
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/tips
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/users
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/remote_jobs
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/remote_files
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/executions
curl --request PUT -d '{"searchClusterId" : "default"}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/doodles

curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/branches/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/cats/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/cities/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/companies/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/configs/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/countries/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/locations/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/manufacturers/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/regions/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/tips/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/users/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/remote_jobs/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/remote_files/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/executions/features/dynamicSchema
curl --request PUT -d '{"enabled" : true}' -H 'Content-type:application/json' http://localhost:8765/api/v1/collections/doodles/features/dynamicSchema

