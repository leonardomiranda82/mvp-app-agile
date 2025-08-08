// src/app/app.ts
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface Message {
  id: number;
  text: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class AppComponent implements OnInit {

  messages: Message[] = []; 
  newMessage: string = '';

  private apiUrl = 'http://localhost:5000/api/messages';

  constructor(private http: HttpClient) {}

  ngOnInit() {
    this.fetchAllMessages();
  }

  fetchAllMessages() { /* ... (sem alterações) ... */ 
    this.http.get<Message[]>(this.apiUrl).subscribe({
      next: (response) => { this.messages = response; },
      error: (error) => { console.error('Falha ao carregar mensagens.', error); }
    });
  }

  onSubmit() { /* ... (sem alterações) ... */
    if (!this.newMessage.trim()) return;
    this.http.post(this.apiUrl, { message: this.newMessage }).subscribe({
      next: () => {
        this.fetchAllMessages();
        this.newMessage = '';
      },
      error: (error) => {
        console.error('Erro ao salvar mensagem!', error);
        alert('Não foi possível salvar a mensagem.');
      }
    });
  }

  // NOVA FUNÇÃO para deletar uma mensagem
  deleteMessage(messageId: number) {
    // Pede confirmação ao usuário
    if (!confirm('Tem certeza que deseja apagar esta mensagem?')) {
      return;
    }

    // Faz uma requisição DELETE para a nova rota, passando o ID
    this.http.delete(`${this.apiUrl}/${messageId}`).subscribe({
      next: () => {
        console.log(`Mensagem ${messageId} deletada com sucesso!`);
        // Após deletar, busca a lista atualizada para atualizar a tela
        this.fetchAllMessages();
      },
      error: (error) => {
        console.error(`Erro ao deletar mensagem ${messageId}!`, error);
        alert('Não foi possível apagar a mensagem.');
      }
    });
  }
}