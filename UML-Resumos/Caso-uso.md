# **Diagrama de Caso de Uso:**

## **Elementos:**

**ATOR:** quem interage com o sistema  

![alt text](./img/caso-uso/caso_01.png)

**CASO DE USO:** funcionalidade que será usada pelo ator  

![alt text](./img/caso-uso/caso_02.png)

**RETÂNGULO:** representa o sistema, ou seja todas os casos de uso ficam dentro dele

## **Relacionamentos:**

**Associação simples:**  

![alt text](./img/caso-uso/caso_03.png)

**\<\<INCLUDE\>\>:**  
Indica um caso de uso que SEMPRE utiliza outro  
**A seta aponta para o caso de uso incluído(caso-pai → caso-filho)**  

![alt text](./img/caso-uso/caso_04.png)

**\<\<EXTEND\>\>**  
Indica um caso opcional ou condicional  
**A seta aponta para o todo(caso-opcional → caso-principal)**  

![alt text](./img/caso-uso/caso_05.png)

**herança:** 
Indica uma herança entre os atores  
**A seta aponta para o todo(ator-filho→ ator-pai)**  

![alt text](./img/caso-uso/caso_06.png)