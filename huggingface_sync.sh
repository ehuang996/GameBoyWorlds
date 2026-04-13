#!/bin/bash
game_names=("pokemon_red" "pokemon_crystal" "pokemon_brown" "pokemon_prism" "pokemon_fools_gold" "pokemon_starbeasts" "sword_of_hope_1" "sword_of_hope_2" "deja_vu_1" "deja_vu_2" "harvest_moon_1" "harvest_moon_2" "harvest_moon_3" "harrypotter_philosophersstone" "legend_of_zelda_links_awakening" "legend_of_zelda_the_oracle_of_seasons")


for game_name in "${game_names[@]}"; do
	echo "Pulling dataset for: $game_name"
	python -m gameboy_worlds.setup_data pull --game "$game_name"
done
