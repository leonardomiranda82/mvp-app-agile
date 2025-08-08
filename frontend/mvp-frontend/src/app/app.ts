// src/app/app.ts
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common'; // Importe CommonModule

@Component({
  selector: 'app-root',
  standalone: true, // <-- Note que ele é standalone
  imports: [CommonModule], // <-- Adicione CommonModule aqui
  templateUrl: './app.html', // <-- O template agora é .html
  styleUrls: ['./app.css']
})
export class AppComponent implements OnInit {

  message: string = 'Carregando mensagem do backend...';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.http.get<{message: string}>('http://localhost:5000/api/message')
      .subscribe({
        next: (response) => { // O que fazer em caso de sucesso
          this.message = response.message;
        },
        error: (error) => { // O que fazer em caso de erro
          this.message = 'Falha ao carregar a mensagem. O backend está de pé?';
          console.error(error);
        }
      });
  }
}