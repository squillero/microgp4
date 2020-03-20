    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$-26095, %eax
    movl	$11636, %ebx
    movl	$-29112, %ecx
    movl	$3883, %edx

    shr $150, %edx
    jnc n11
    jmp n32
    sub %eax, %edx
    or %edx, %edx
    jmp n15
    shl $13, %edx
    shl $98, %eax
n11:
    add %eax, %eax
    xor %ebx, %ebx
    jno n22
    jc n28
n15:
    or %edx, %ebx
    je n21
    add %eax, %ebx
    jne n37
    or %ecx, %ecx
    shr $75, %edx
n21:
    jne n41
n22:
    jc n32
    shl $4, %ebx
    shr $121, %eax
    or %ecx, %ebx
    je n33
    shr $174, %ebx
n28:
    cmp %edx, %edx
    shl $171, %ecx
    jnc n36
    jnz n33
n32:
    jo n33
n33:
    jo n37
    add %ebx, %ebx
    or %ebx, %ebx
n36:
    shl $169, %edx
n37:
    je n41
    jnz n39
n39:
    jc n40
n40:
    add %ecx, %eax
n41:
    jno n42
n42:
    sub %ecx, %edx
    shr $184, %eax
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
