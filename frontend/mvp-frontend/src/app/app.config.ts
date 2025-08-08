// src/app/app.config.ts
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient } from '@angular/common/http'; // <-- IMPORTE AQUI

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient() // <-- ADICIONE AQUI
  ]
};