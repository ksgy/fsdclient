callsign = "MIS"
password = ""
homebase = "LHBP"



DataRef( "xpdr_f", "sim/cockpit/radios/transponder_mode", "readonly" )
DataRef( "xpdr", "sim/cockpit/radios/transponder_code", "readonly" )
DataRef( "alt", "sim/cockpit2/gauges/indicators/altitude_ft_pilot", "readonly" )
DataRef( "lat", "sim/flightmodel/position/latitude", "readonly" )
DataRef( "lon", "sim/flightmodel/position/longitude", "readonly" )
DataRef( "spd", "sim/cockpit2/gauges/indicators/airspeed_kts_pilot", "readonly" )
DataRef( "hdg", "sim/cockpit/autopilot/heading", "readonly" )


function fsdclient()
	infofile = io.open(SCRIPT_DIRECTORY.."fsdclient.txt", "w")
	io.output(infofile)
	io.write(xpdr_f .. "|" .. xpdr .. "|" .. alt .. "|" .. lat .. "|" .. lon .. "|" .. spd .. "|" .. hdg .. "|" .. callsign .. "|" .. password .. "|" .. homebase)
	io.close(infofile)
end

-- do_sometimes("fsdclient()")
do_often("fsdclient()")