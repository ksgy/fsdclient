callsign = "MIS"
password = ""
homebase = "LHBP"



DataRef( "HH_heading", "sim/cockpit/autopilot/heading", "readonly" )
-- transponder flag
-- sqawk
-- alt
-- lat
-- lon
-- spd
-- hdg

last_heading = HH_heading


function fsdclient()


	infofile = io.open(SCRIPT_DIRECTORY.."fsdclient.txt", "w")
	io.output(infofile)
	io.write('heading: ' .. last_heading)
	io.close(infofile)
	
end

-- do_sometimes("fsdclient()")
do_every_frame("fsdclient()")