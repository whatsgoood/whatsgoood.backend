import { Component, OnInit } from '@angular/core';
import { SportService } from './sport.service';
import { Sport } from './sport.model';

@Component({
  selector: 'app-sport',
  templateUrl: './sport.component.html',
  styleUrls: ['./sport.component.scss']
})
export class SportComponent implements OnInit {
  public sports: Sport[];

  constructor(
    private sportService: SportService
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
  }

  private populateSportCards(sports: Sport[]) {
    this.sports = sports.sort((a, b) => b.rating - a.rating);
  }

  public ratingClass(rating: number) {
    if (rating > 6) {
      return { 'card-green': true }
    } else if (rating > 3) {
      return { 'card-orange': true}
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
