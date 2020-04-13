import { Component, OnInit } from '@angular/core';
import { SportService } from './sport.service';
import { Sport } from './sport.model';
import { WeatherService } from '../weather/weather.service';
import { Weather } from '../weather/weather.model';

@Component({
    selector: 'app-sport',
    templateUrl: './sport.component.html',
    styleUrls: ['./sport.component.scss']
})
export class SportComponent implements OnInit {
    public sports: Sport[];
    public weather: Weather;

    constructor(
        private sportService: SportService,
        private weatherService: WeatherService
    ) { }

    ngOnInit(): void {
        this.sportService.getSportList()
            .subscribe(
                data => {
                    this.populateSportCards(data);
                },
                error => {
                    console.log('UI display... ', error);
                }
            );

        this.weatherService.getWeather()
            .subscribe(
                data => {
                    this.populateWeather(data);
                },
                error => {
                    console.log('UI display... ', error);
                }
            );
    }

    private populateSportCards(sports: Sport[]) {
        this.sports = sports.sort((a, b) => b.rating - a.rating);
    }

    private populateWeather(weather: Weather) {
        this.weather = weather;
        console.log('Weather summary: ', this.weather);
    }

    public ratingClass(rating: number) {
        if (rating > 6) {
            return { 'card-green': true }
        } else if (rating > 3) {
            return { 'card-orange': true }
        } else {
            return { 'card-red': true }
        }
    }

    public isKiting(name: string) {
        return name === 'Kiting';
    }

    public isSurfing(name: string) {
        return name === 'Surfing';
    }

    public isClimbing(name: string) {
        return name === 'Climbing';
    }

}
