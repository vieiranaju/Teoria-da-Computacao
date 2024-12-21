// O problema envolve a criação de um sistema de recomendação de livros baseado em informações como título, gênero, número de páginas e avaliação. 
// Para atender aos requisitos, o código realiza as seguintes tarefas:
// 1. Extrai os títulos dos livros de uma lista fornecida.
// 2. Filtra os livros com avaliações acima de 4 para destacar os mais bem avaliados.
// 3. Calcula o número total de páginas dos livros filtrados.
using System;
using System.Collections.Generic;
using System.Linq;

class Livro
{
    public string Titulo { get; set; }
    public string Genero { get; set; }
    public int Paginas { get; set; }
    public double Avaliacao { get; set; }
}

class Program
{
    static void Main(string[] args)
    {
        // Lista de livros
        var livros = new List<Livro>
        {
            new Livro { Titulo = "Percy Jackson", Genero = "Fantasia", Paginas = 375, Avaliacao = 4.5 },
            new Livro { Titulo = "Os Sete Maridos de Evelyn Hugo", Genero = "Drama", Paginas = 400, Avaliacao = 4.8 },
            new Livro { Titulo = "Frankenstein", Genero = "Terror", Paginas = 280, Avaliacao = 4.1 },
            new Livro { Titulo = "A Hora da Estrela", Genero = "Ficção", Paginas = 87, Avaliacao = 3.9 },
            new Livro { Titulo = "1984", Genero = "Distopia", Paginas = 328, Avaliacao = 4.7 }
        };

        // 1. Criar uma lista com apenas os títulos dos livros
        var titulos = livros.Select(livro => livro.Titulo).ToList();
        Console.WriteLine("Titulos dos Livros:");
        titulos.ForEach(Console.WriteLine);

        // 2. Filtrar livros com avaliação acima de 4
        var livrosBemAvaliados = livros.Where(livro => livro.Avaliacao > 4).ToList();
        Console.WriteLine("\nLivros Bem Avaliados (Acima de 4):");
        livrosBemAvaliados.ForEach(livro => Console.WriteLine($"{livro.Titulo} - {livro.Avaliacao}"));

        // 3. Calcular o total de páginas dos livros selecionados (usando Aggregate, equivalente ao reduce)
        var totalPaginas = livrosBemAvaliados.Aggregate(0, (total, livro) => total + livro.Paginas);
        Console.WriteLine($"\nTotal de Paginas dos Livros Bem Avaliados: {totalPaginas}");
    }
}
