require 'sequel'
require "reel"

if RUBY_PLATFORM == 'java'
  conn = { :adapter => 'jdbc', :jndi => 'java:comp/env/jdbc/hello_world', :pool => 256 }
else
  conn = { :adapter => 'mysql2', :database => 'hello_world', :username => 'benchmarkdbuser', :password => 'benchmarkdbpass', :host => 'localhost', :pool => 256, :timeout => 5000 }
end

DB = Sequel.connect(conn)

addr, port = '127.0.0.1', 8080

Reel::Server.run(addr, port) do |connection|
  while request = connection.request

    if request.url == "/db"
      queries = (params[:queries] || 1).to_i

      results = (1..queries).map do
        DB[:world].find(Random.rand(10000) + 1)
      end
      connection.respond :ok, results.to_json
    else
      connection.respond :ok, "Hello, World!"
    end
  end
end
