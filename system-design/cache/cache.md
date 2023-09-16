## cache aside
- appplication is responsilbe for reading & writing from the storage and cache doesn't interact with the storage at all.

## write through
- application treats cache as main data store
- cache is responsible for reading & writing this to database

## write behind
- modify the cache entry and asynchronously written to database

## refresh ahead
- cache asynchronously reload (refresh) the data before it is close to expiration