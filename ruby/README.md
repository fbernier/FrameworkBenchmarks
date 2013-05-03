# Ruby Benchmarking Test

This is the Ruby portion of a [benchmarking test suite](../) comparing a variety of web development platforms.

### JSON Encoding Test
* [JSON test source](hello_world.rb)

### Data-Store/Database Mapping Test

* [Database test source](hello_world.rb)

## Infrastructure Software Versions
The tests were run with:
* [Ruby 2.0.0-p0](http://www.ruby-lang.org/)
* [JRuby 1.7.3](http://jruby.org/)
* [Reel 0.4.0.pre](http://www.celluloid.io/)
* [Resin 4.0.34](http://www.caucho.com/)
* [MySQL 5.5.29](https://dev.mysql.com/)

## Test URLs

### JSON Encoding Test

Ruby:
localhost:8080/json

JRuby:
localhost:8080/jruby/json

### Data-Store/Database Mapping Test

Ruby:
localhost:8080/db?queries=5

JRuby:
localhost:8080/jruby/db?queries=5
