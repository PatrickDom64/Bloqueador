# 🔒 Bloqueador de Sites - Python + Tkinter

Este é um programa simples feito em Python que permite **bloquear e desbloquear sites** diretamente do seu computador, por meio de uma interface gráfica amigável criada com `Tkinter`.

Ideal para:
- Aumentar a produtividade.
- Restringir distrações (como redes sociais ou YouTube).
- Criar rotinas de estudo ou trabalho.

---

## 🖼️ Interface Gráfica

A interface permite:

✅ Inserir uma lista de sites para bloquear  
✅ Bloquear/desbloquear com um clique  
✅ Ver os sites atualmente bloqueados  

![screenshot do app](#) *(adicione imagem depois, se quiser)*

---

## ⚙️ Como funciona?

O programa edita o arquivo `hosts` do sistema operacional, redirecionando os sites indesejados para `127.0.0.1`, o que impede o acesso pelo navegador.

Exemplo de linha adicionada ao arquivo:


---

## 🛠️ Requisitos

- Python 3.x
- Sistema operacional:
  - Windows (recomendado)
  - Linux/macOS (com pequenas adaptações)
- Acesso de **administrador/root** (necessário para editar o arquivo `hosts`)
