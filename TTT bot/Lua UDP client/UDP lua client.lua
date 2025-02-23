#!/usr/bin/env lua5.2
--
-- apt install lua5.2 lua-socket
--

local socket = require("socket")
local udp = assert(socket.udp())
local data

udp:settimeout(1)
assert(udp:setsockname("*",0))
assert(udp:setpeername("",41234))

for i = 0, 2, 1 do
  assert(udp:send("Hello chris"))
  data = udp:receive()
  if data then
    break
  end
end


if data == nil then
  print("timeout")
else
  print(data)
end