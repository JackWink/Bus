#Bus

Bus is a small commandline script that pulls down and parses Ann Arbor's AATA current bus schedule.

##Usage

    jackmac:~ jackwink$ bus 2
    
    
    Direction             Arriving                        Location                       Next Stop   Time 

    -------------------------------------------------------------------------------------------------------
    From Downtown     1 min behind   Central Campus Transit Center                     UMH Taubman   3:31
    From Downtown          On time            Blake Transit Center   Central Campus Transit Center   3:39
    From Downtown     3 min behind             Plymouth and Barton                   Plymouth Mall   3:30
    To Downtown            On time             Plymouth and Barton                     UMH Taubman   3:31
    
    
	jackmac:~ jackwink$


##Dependencies

- Requests

##Installation

If you don't have requests installed, install it! `pip install requests`

Move `bus.py` to `/usr/local/bin/` or `/usr/bin/` and rename it bus.  Make sure you set `chmod +x bus` for it to execute.
