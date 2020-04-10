import { Component } from '@angular/core';
import { SportService } from './sport.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'WhatsGood';

  constructor(
    private sportService: SportService
  ) {
    this.sportService.getSportList()
      .subscribe(
        data => { console.log('Le data shire... \n', data); },
        error => { console.log('UI display... ', error); }
      );

  }

}
