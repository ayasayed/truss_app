import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HeadComponent } from './head/head.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {FlexLayoutModule} from '@angular/flex-layout';
import { MatTabsModule, MatSidenavModule, MatToolbarModule ,MatIconModule,MatListModule , MatButtonModule} from '@angular/material';
import { HeaderComponent } from './navigation/header/header.component';
import { SidenavListComponent } from './navigation/sidenav-list/sidenav-list.component';
import { FixedsidnavComponent } from './fixedsidnav/fixedsidnav.component';

@NgModule({
  declarations: [
    AppComponent,
    HeadComponent,
    HeaderComponent,
    SidenavListComponent,
    FixedsidnavComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FlexLayoutModule,
    MatTabsModule,
     MatSidenavModule,
     MatToolbarModule,
     MatIconModule,
      MatButtonModule,
      MatListModule
  ],
  exports:[
    MatTabsModule,
    MatSidenavModule,
     MatToolbarModule,
     MatIconModule,
     MatButtonModule,
     MatListModule
    ],

  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
